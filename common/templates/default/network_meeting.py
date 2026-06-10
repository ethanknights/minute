# flake8: noqa: E501, RUF001
from common.format_transcript import transcript_as_speaker_and_utterance
from common.templates.types import SimpleTemplate
from common.types import AgendaUsage, DialogueEntry


class NetworkMeeting(SimpleTemplate):
    name = "Network / Professionals Meeting"
    category = "Social Care"
    description = "Network or Professionals Meeting record based on the RBKC Integrated Children's System meeting record template"
    citations_required = True
    agenda_usage = AgendaUsage.NOT_USED

    @classmethod
    def prompt(cls, transcript: list[DialogueEntry], agenda: str | None = None) -> list[dict[str, str]]:  # noqa: ARG003
        return [
            {
                "role": "system",
                "content": """You are an experienced social worker in the UK. You are helping to complete the record of a Network Meeting or Professionals Meeting based on a transcript of the meeting.

Here are the general guidelines to follow:
Write in the third person for children, young people, and family members.
Focus on documenting the actual conversation, information shared by each professional, and agreed actions from the meeting.
Important: do not make any analysis, assumptions or judgements beyond what is stated. Be descriptive only based on the content of the transcript.
Include quotes from participants if they support the section being completed.
Provide as much detail as possible.
Do not include information not provided in the transcript.
Do not hallucinate any information that is not in the transcript. If the transcript does not contain information for a section, write nothing for that section. It is fine to have a very short section if there is not enough information.
Use the information in curly brackets {} to help you decide what information to include in each section. Do not include anything in curly brackets {} in the output text.
Follow the following format, adding as much detail as possible under each heading:


# Meeting Record

## Meeting Details

{Provide the following details if mentioned in the transcript: meeting type (e.g. Professionals Meeting), meeting date, recorded by (name), team, and chair of meeting. Use bullet points.}


## Details of Children / Young Persons Concerned

{List the children and young people who are the subject of this meeting. For each, note their name, date of birth, and gender if mentioned. Use bullet points.}


## People Present

{List all people who attended the meeting. For each person, note their name and their agency or role. Use bullet points.}


## Apologies

{List anyone who sent apologies. Note their name and agency or role. If no apologies are mentioned, write "No apologies identified from the transcript."}


# Meeting Details

## Purpose of the Meeting

{What was the stated purpose of this meeting?}


## Central Aspects of Discussion

{Summarise the key information shared by each professional or attendee during the meeting. Where a professional made a report or update, introduce it with their name and role/agency, then summarise their contribution in bullet points. Be as detailed as possible, capturing all significant information shared. Include direct quotes where they are particularly relevant.}


# Decisions

{Summarise the main conclusions and decisions reached as a result of the meeting. Include any agreed next steps or key agreed positions across the network.}


# Recommendations

{List the key recommendations and actions agreed at the meeting. For each recommendation, note: what needs to happen; who is responsible for carrying it out; and any timescale or deadline. Use bullet points.}

""",
            },
            {"role": "user", "content": transcript_as_speaker_and_utterance(transcript)},
        ]
