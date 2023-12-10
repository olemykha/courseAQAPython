"""HOMEWORK2."""
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

# Example %-format from teacher
norway_text = (
    'Automatisering akselererer %syeblikket da '
    'roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
)
logging.info(norway_text)

norwegian_letter_ue = 'ø'
norwegian_letter_o = 'å'
norwegian_letter_eh = 'Æ'

# Using str.format()
norway_text_with_format_call = (
    'Automatisering akselererer {0}yeblikket da '
    'roboter vil erobre planeten v{1}r. ({2})'
).format(norwegian_letter_ue, norwegian_letter_o, norwegian_letter_eh)
logging.info(norway_text_with_format_call)

# Using f-string
norway_text_with_fstring_format = (
    f'Automatisering akselererer {norwegian_letter_ue}yeblikket da '
    f'roboter vil erobre planeten v{norwegian_letter_o}r. '
    f'({norwegian_letter_eh})'
)
logging.info(norway_text_with_fstring_format)
