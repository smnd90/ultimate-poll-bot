"""Callback functions needed during creation of a Poll."""
from pollbot.helper.update import remove_poll_messages, update_poll_messages


def delete_poll(session, context):
    """Permanently delete the pall."""
    remove_poll_messages(session, context.bot, context.poll)
    session.delete(context.poll)
    session.commit()


def close_poll(session, context):
    """Close this poll."""
    context.poll.closed = True
    session.commit()
    update_poll_messages(session, context.bot, context.poll)


def reopen_poll(session, context):
    """Reopen this poll."""
    context.poll.closed = False
    session.commit()
    update_poll_messages(session, context.bot, context.poll)