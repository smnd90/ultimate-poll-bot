"""Callback functions needed during creation of a Poll."""
from pollbot.helper.display.creation import get_init_text, get_vote_type_help_text
from pollbot.helper.creation import create_poll
from pollbot.helper.enums import VoteType, ExpectedInput
from pollbot.telegram.keyboard import (
    get_change_vote_type_keyboard,
    get_init_keyboard,
)

from pollbot.models import Poll


def show_vote_type_keyboard(session, context):
    """Show to vote type keyboard."""
    poll = session.query(Poll).get(context.payload)

    keyboard = get_change_vote_type_keyboard(poll)
    context.query.message.edit_text(get_vote_type_help_text(poll), parse_mode='markdown', reply_markup=keyboard)


def change_vote_type(session, context):
    """Change the vote type."""
    context.poll.vote_type = VoteType(context.action).name

    keyboard = get_init_keyboard(context.poll)
    context.query.message.edit_text(
        get_init_text(context.poll),
        parse_mode='markdown',
        reply_markup=keyboard
    )


def toggle_anonymity(session, context):
    """Change the anonymity settings of a poll."""
    context.poll.anonymous = not context.poll.anonymous

    keyboard = get_init_keyboard(context.poll)
    context.query.message.edit_text(
        get_init_text(context.poll),
        parse_mode='markdown',
        reply_markup=keyboard
    )


def toggle_results_visible(session, context):
    """Change the results visible settings of a poll."""
    context.poll.results_visible = not context.poll.results_visible

    keyboard = get_init_keyboard(context.poll)
    context.query.message.edit_text(
        get_init_text(context.poll),
        parse_mode='markdown',
        reply_markup=keyboard
    )


def all_options_entered(session, context):
    """All options are entered the poll is created."""
    if context.poll is None:
        return

    if context.poll.vote_type in [VoteType.limited_vote.name, VoteType.cumulative_vote.name]:
        context.poll.expected_input = ExpectedInput.vote_count.name
        context.query.message.chat.send_message('Send me the amount of allowed votes per user.')

        return

    create_poll(session, context.poll, context.user, context.query.message.chat, context.query.message)
