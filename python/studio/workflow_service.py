from python.research.research_service import ResearchService
from python.script.script_service import ScriptService
from python.scene.scene_service import SceneService

from python.config.settings import settings


class WorkflowService:

    def run(self, topic: str):

        research_service = ResearchService()
        script_service = ScriptService()
        scene_service = SceneService()

        print("Generating Research...")

        research = research_service.generate_research(topic)

        print("Generating Script...")

        # Script now uses research output
        script = script_service.generate_script(research)

        # Replace Telegram placeholder
        script = script.replace(
            "[TELEGRAM_LINK]",
            settings.TELEGRAM_LINK
        )

        print("Generating Scenes...")

        scenes = scene_service.generate_scene(script)

        return {
            "topic": topic,
            "research": research,
            "script": script,
            "scenes": scenes
        }