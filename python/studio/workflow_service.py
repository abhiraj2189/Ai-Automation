from python.research.research_service import ResearchService
from python.script.script_service import ScriptService
from python.scene.scene_service import SceneService
from python.config.settings import settings


class WorkflowService:

    def run(self, topic: str):

        try:
            print("Generating Research...")
            research = ResearchService().generate_research(topic)
            print("Research Done")

            print("Generating Script...")
            script = ScriptService().generate_script(research)
            print("Script Done")

            script = script.replace(
                "[TELEGRAM_LINK]",
                settings.TELEGRAM_LINK
            )

            print("Generating Scenes...")
            scenes = SceneService().generate_scene(script)
            print("Scenes Done")

            return {
                "topic": topic,
                "research": research,
                "script": script,
                "scenes": scenes
            }

        except Exception as e:
            print("WORKFLOW ERROR:", e)
            raise