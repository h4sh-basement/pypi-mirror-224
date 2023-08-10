from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db.models import QuerySet
from django.http import HttpRequest
from django.urls import reverse
from django.utils import timezone
from .app_settings import app_settings
from .forms import UserSwitchForm
from .models import SimulatedUserSession


UserModel = get_user_model()


# noinspection PyProtectedMember
def simulate_user_context(request: HttpRequest) -> dict[str, any]:
    """
    Context Processor: simulate_user_context

    Provides context variables related to the user simulation feature in the app.

    Parameters:
    - request (HttpRequest): The current HttpRequest object.

    Returns:
    - dict: A dictionary containing the necessary context variables.

    Context Variables:
    - simulate_user_form (UserSwitchForm): The form used to switch or simulate different users.
    - switch_simulated_user_url (str): The URL endpoint for switching simulated users.
    - show_simulated_user_control_bar (bool): Indicates if the simulation control bar should be shown.
    - simulated_user_control_bar_enabled (bool): Indicates if the control bar is active/enabled.
    - time_since_last_change: Indicates the time passed since the last simulation change.

    Functionality:
    - Determines the current state of the user, whether they are in a simulation or not.
    - Checks conditions and settings to decide the visibility and activity state of the simulation control bar.
    - Sets the initial data for the UserSwitchForm based on the current simulation state.

    Usage:
    This context processor should be added to the 'context_processors' option in Django's template settings to
    ensure that the required context variables are available in every template.
    """
    control_condition: bool = getattr(request.real_user, app_settings.SIMULATED_USER_CONTROL_CONDITION, False)
    primary_key_name: str = UserModel._meta.pk.name
    if isinstance(request.user, AnonymousUser):
        simulated_user_pk: str = 'unauthenticated'
    elif request.user != request.real_user:
        simulated_user_pk: str | int = getattr(request.user, primary_key_name)
    else:
        simulated_user_pk: None = None
    if control_condition:
        records: QuerySet[SimulatedUserSession] = SimulatedUserSession.objects.filter(
            real_session_key=request.session.session_key
        )
        results_1: bool = records.filter(hide_bar=True).exists()

        records: QuerySet[SimulatedUserSession] = SimulatedUserSession.objects.filter(
            simulated_session_key=request.session.session_key
        )
        results_2: bool = records.filter(hide_bar=True).exists()
        hide_bar: bool = results_1 or results_2
    else:
        hide_bar: bool = True
    try:
        simulated_session: SimulatedUserSession = SimulatedUserSession.objects.get(
            simulated_session_key=request.session.session_key
        )
        time_since_last_change: timedelta = timezone.now() - simulated_session.created_at
    except SimulatedUserSession.DoesNotExist:
        time_since_last_change: str = "Not in a simulation"

    form_initial_data: dict[str, any] = {
        'user_pk': simulated_user_pk if simulated_user_pk != 'unauthenticated' else None,
        'username': '',
        'email': '',
        'unauthenticated': simulated_user_pk == 'unauthenticated',
        'enabled': simulated_user_pk is not None,
        'hide': hide_bar
    }
    form: UserSwitchForm = UserSwitchForm(initial=form_initial_data)

    if control_condition:
        show_bar: bool = not hide_bar
    else:
        show_bar: bool = False

    if not show_bar:
        bar_enabled: bool = False
    else:
        bar_enabled: bool = simulated_user_pk is not None

    if not app_settings.ONLY_ALLOW_SIMULATED_GET_REQUESTS:
        bar_enabled: bool = False

    context: dict[str, any] = {
        'simulate_user_form': form,
        'switch_simulated_user_url': reverse('simulate_user_switch_user'),
        'show_simulated_user_control_bar': show_bar,
        'simulated_user_control_bar_enabled': bar_enabled,
        'time_since_last_change': time_since_last_change
    }

    return context
