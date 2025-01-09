from django import template

register = template.Library()

@register.inclusion_tag('main/messages_tags.html')
def show_messages(messages):
    return {'messages': messages}