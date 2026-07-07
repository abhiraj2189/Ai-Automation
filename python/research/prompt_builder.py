class PromptBuilder:

    @staticmethod
    def build(topic: str):

        return f"""
You are an expert Tech Research Assistant.

Research this topic:

{topic}

Return the response in this format:

1. Introduction

2. Latest Information

3. Important Features

4. Advantages

5. Disadvantages

6. Real World Uses

7. Future Scope

8. Summary

Write professionally.
"""