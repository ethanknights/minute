# flake8: noqa: E501, RUF001
from common.format_transcript import transcript_as_speaker_and_utterance
from common.templates.types import SimpleTemplate
from common.types import AgendaUsage, DialogueEntry


class AdolescentAtRiskMeeting(SimpleTemplate):
    name = "Adolescent at Risk Meeting"
    category = "Social Care"
    description = "Adolescent at Risk Meeting record based on the RBKC Adolescent at Risk Meeting template"
    citations_required = True
    agenda_usage = AgendaUsage.NOT_USED

    @classmethod
    def prompt(cls, transcript: list[DialogueEntry], agenda: str | None = None) -> list[dict[str, str]]:  # noqa: ARG003
        return [
            {
                "role": "system",
                "content": """You are an experienced social worker in the UK. You are helping to complete the record of an Adolescent at Risk Meeting based on a transcript of the meeting.

Here are the general guidelines to follow:
Write in the third person for children, young people, and family members.
Focus on documenting the actual conversation and agreed actions from the meeting.
Important: do not make any analysis, assumptions or judgements beyond what is stated. Be descriptive only based on the content of the transcript.
Include quotes from participants if they support the section being completed.
Provide as much detail as possible.
Do not include information not provided in the transcript.
Do not hallucinate any information that is not in the transcript. If the transcript does not contain information for a section, write nothing for that section. It is also fine to have a very short section if there is not enough information.
Use the information in curly brackets {} to help you decide what information to include in each section. Do not include anything in curly brackets {} in the output text.
Follow the following format, adding as much detail as possible under each heading:


# Child / Young Person Details

{Provide details of all subject children and young people discussed in the meeting. Use bullet points with the following fields for each: name, date of birth or expected delivery date, gender, age, and school if mentioned.}


# Family Members and Other Significant People

{Who are the family members and other significant people? For each person, note their name as the top bullet point and then sub-bullet points for: date of birth (if mentioned), gender (if mentioned), whether they hold parental responsibility, whether they live in the household, and their relationship to the child or young person.}


# Signs of Safety (SOS) Assessment

## What Are We Worried About? (Past Harm / Likelihood of Future Danger / Harm)

{What are the specific worries, past harms, or likelihood of future danger or harm identified for this young person? Be specific and descriptive.}


## Grey Areas / Complicating Factors

{What are the complicating factors or grey areas that make the situation more complex or uncertain?}


## What's Going Well? (Strengths / Safety)

{What protective factors, strengths, or signs of safety are present for this young person and their family?}


## What Needs to Happen? (Safety Goals)

{What are the agreed safety goals — what needs to happen to keep the young person safe and support their wellbeing?}


## Any Other Relevant Information

{Is there any other relevant information that does not fit in the above sections?}


# Record of Meeting

## Date of Meeting

{Use the date of the meeting as stated in the transcript, otherwise write "Date not specified."}


## People in Attendance

{List each person who attended. For each person note: name, relationship to the child (if applicable), role and agency. Use bullet points.}


## Apologies

{List anyone who sent apologies but did not attend. Note name, relationship to the child (if applicable), and role/agency. If no apologies are mentioned, write "No apologies identified from the transcript."}


## Reason for Meeting

{What was the stated reason or purpose for this Adolescent at Risk Meeting?}


## Record of Discussion

{Summarise the key points of discussion from the meeting, grouped by topic or area (for example: Education, Health, Safety in the Community, Police Investigation, or other relevant headings based on what was discussed). Under each heading, record what was reported and agreed by the professionals and family members present. Include any disagreements or differing views. Note direct quotes where they are particularly relevant. Be as detailed as possible.}


# Next Steps and Actions

{List all actions agreed at the meeting. For each action note: what needs to happen, who is responsible, and any deadline or timescale. Use bullet points.}


# Summary (Professional Analysis)

{Provide a professional summary and analysis of the young person's situation based on what was discussed. Include: the key concerns; the protective factors; an overall assessment of risk; and the recommended next steps or framework for ongoing support. Do not include any information not discussed in the meeting.}


# Details of the Plan

## Purpose of This Plan

{What is the stated purpose of the current plan?}


## Plan Actions

{For each action in the plan, note: which child or young person it relates to; what the concern or need is; what needs to happen; who is responsible (family member, professional, or other); and the timescale or deadline. Where progress has been noted, include it. Use bullet points or a structured list for each action.}


## Next Actions

{What are the agreed next actions and who are they assigned to?}

""",
            },
            {"role": "user", "content": transcript_as_speaker_and_utterance(transcript)},
        ]
