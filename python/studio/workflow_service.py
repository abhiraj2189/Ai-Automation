from python.research.research_service import ResearchService
from python.script.script_service import ScriptService
from python.scene.scene_service import SceneService

from python.voice.voice_service import VoiceService
from python.subtitles.subtitle_service import SubtitleService
from python.assets.asset_service import AssetService
from python.renderer.renderer_service import RendererService

from python.progress.progress_manager import ProgressManager
from python.config.settings import settings


class WorkflowService:

    def run(
        self,
        topic: str,
        job_id: str | None = None
    ):

        try:

            # ---------------------------------
            # Research
            # ---------------------------------

            if job_id:
                ProgressManager.update(
                    job_id,
                    "Generating Research",
                    10
                )

            print("Generating Research...")

            research = ResearchService().generate_research(topic)

            print("Research Done")

            # ---------------------------------
            # Script
            # ---------------------------------

            if job_id:
                ProgressManager.update(
                    job_id,
                    "Generating Script",
                    25
                )

            print("Generating Script...")

            script = ScriptService().generate_script(research)

            script = script.replace(
                "[TELEGRAM_LINK]",
                settings.TELEGRAM_LINK
            )

            print("Script Done")

            # ---------------------------------
            # Scene
            # ---------------------------------

            if job_id:
                ProgressManager.update(
                    job_id,
                    "Generating Scene",
                    40
                )

            print("Generating Scene...")

            scenes = SceneService().generate_scene(script)

            print("Scene Done")

            # ---------------------------------
            # Voice
            # ---------------------------------

            if job_id:
                ProgressManager.update(
                    job_id,
                    "Generating Voice",
                    55
                )

            print("Generating Voice...")

            voice = VoiceService().generate(

                text=script,

                output="outputs/audio/output.mp3",

                language="hindi_male"

            )

            print("Voice Done")

            # ---------------------------------
            # Subtitle
            # ---------------------------------

            if job_id:
                ProgressManager.update(
                    job_id,
                    "Generating Subtitle",
                    70
                )

            print("Generating Subtitle...")

            subtitle = SubtitleService().generate(
                voice
            )

            print("Subtitle Done")

            # ---------------------------------
            # Assets
            # ---------------------------------

            if job_id:
                ProgressManager.update(
                    job_id,
                    "Downloading Assets",
                    85
                )

            print("Downloading Assets...")

            assets = AssetService().download(
                keyword=topic,
                type="video",
                count=5
            )

            videos = [
                item["path"]
                for item in assets
            ]

            print("Assets Done")

            # ---------------------------------
            # Renderer
            # ---------------------------------

            if job_id:
                ProgressManager.update(
                    job_id,
                    "Rendering Final Video",
                    95
                )

            print("Rendering Video...")

            result = RendererService().render(

                audio=voice,

                subtitle=subtitle,

                videos=videos,

                output="outputs/final/final_video.mp4"

            )

            print("Render Done")

            if job_id:
                ProgressManager.complete(job_id)

            return {

                "success": True,

                "topic": topic,

                "research": research,

                "script": script,

                "scenes": scenes,

                "audio": voice,

                "subtitle": subtitle,

                "videos": videos,

                "result": result

            }

        except Exception as e:

            print("=" * 70)
            print("WORKFLOW ERROR")
            print(e)
            print("=" * 70)

            if job_id:

                ProgressManager.update(
                    job_id,
                    "Failed",
                    0,
                    status="Failed"
                )

            raise