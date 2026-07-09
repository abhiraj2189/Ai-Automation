from python.jobs.job_manager import JobManager

from python.research.research_service import ResearchService
from python.script.script_service import ScriptService
from python.scene.scene_service import SceneService
from python.voice.voice_service import VoiceService
from python.subtitles.subtitle_service import SubtitleService
from python.assets.asset_service import AssetService
from python.composer.composer_service import ComposerService

from python.config.settings import settings


class WorkflowService:

    def run(

        self,

        topic: str,

        job_id: str = None

    ):

        try:

            # -----------------------------
            # Research
            # -----------------------------

            if job_id:
                JobManager.update(
                    job_id,
                    10,
                    "Generating Research"
                )

            research = ResearchService().generate_research(topic)

            # -----------------------------
            # Script
            # -----------------------------

            if job_id:
                JobManager.update(
                    job_id,
                    25,
                    "Generating Script"
                )

            script = ScriptService().generate_script(research)

            script = script.replace(
                "[TELEGRAM_LINK]",
                settings.TELEGRAM_LINK
            )

            # -----------------------------
            # Scene
            # -----------------------------

            if job_id:
                JobManager.update(
                    job_id,
                    40,
                    "Generating Scenes"
                )

            scenes = SceneService().generate_scene(script)

            # -----------------------------
            # Voice
            # -----------------------------

            if job_id:
                JobManager.update(
                    job_id,
                    55,
                    "Generating Voice"
                )

            voice = VoiceService().generate(script)

            # -----------------------------
            # Subtitle
            # -----------------------------

            if job_id:
                JobManager.update(
                    job_id,
                    65,
                    "Generating Subtitle"
                )

            subtitle = SubtitleService().generate(
                voice["audio"]
            )

            # -----------------------------
            # Assets
            # -----------------------------

            if job_id:
                JobManager.update(
                    job_id,
                    80,
                    "Downloading Assets"
                )

            assets = AssetService().download(

                keyword=topic,

                count=5

            )

            videos = [

                item["path"]

                for item in assets

            ]

            # -----------------------------
            # Render
            # -----------------------------

            if job_id:
                JobManager.update(
                    job_id,
                    95,
                    "Rendering Video"
                )

            result = ComposerService().generate(

                audio=voice["audio"],

                subtitle=subtitle["subtitle"],

                videos=videos,

                output="outputs/final/final_video.mp4"

            )

            if job_id:

                JobManager.complete(

                    job_id,

                    result["video"]

                )

            return {

                "topic": topic,

                "research": research,

                "script": script,

                "scenes": scenes,

                "voice": voice,

                "subtitle": subtitle,

                "assets": assets,

                "video": result["video"]

            }

        except Exception as e:

            if job_id:

                JobManager.failed(

                    job_id,

                    str(e)

                )

            raise