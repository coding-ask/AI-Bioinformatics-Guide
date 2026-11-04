from pydantic import BaseModel, Field


class BioinformaticsResponse(BaseModel):

    core_explanation: str = Field(
        description="A direct, accurate answer to the user's bioinformatics question"
    )

    fundamentals: str = Field(
        description="Underlying biological, mathematical or computational concepts needed to understand the topic"
    )

    how_it_works: str = Field(
        description="Step-by-step explanation of the mechanism, algorithm or workflow"
    )

    practical_example: str = Field(
        description="An illustrative biological, computational, command-line or coding example when relevant"
    )

    tools_and_databases: str = Field(
        description="Relevant bioinformatics tools, software and databases, with their purposes"
    )

    related_concepts: str = Field(
        description="Closely related concepts the learner should understand next"
    )

    further_learning: str = Field(
        description="Useful next learning steps and authoritative resources by name, without fabricated references"
    )
