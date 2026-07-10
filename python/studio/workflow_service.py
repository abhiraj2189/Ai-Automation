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

    def run(self, topic: str, job_id: str = None):

        try:

            print("\n==============================")
            print("🚀 AI AUTOMATION WORKFLOW START")
            print("TOPIC :", topic)
            print("==============================\n")

            # ======================================
            # RESEARCH
            # ======================================

            print("🔎 STEP 1 : Research")

            if job_id:
                JobManager.update(job_id, 10, "Generating Research")

            research = ResearchService().generate_research(topic)

            print("✅ Research Completed")

            # ======================================
            # SCRIPT
            # ======================================

            print("\n📝 STEP 2 : Script")

            if job_id:
                JobManager.update(job_id, 25, "Generating Script")

            script = ScriptService().generate_script(research)

            script = script.replace(
                "[TELEGRAM_LINK]",
                settings.TELEGRAM_LINK
            )

            print("✅ Script Completed")

            # ======================================
            # SCENE
            # ======================================

            print("\n🎬 STEP 3 : Scene")

            if job_id:
                JobManager.update(job_id, 40, "Generating Scene")

            scenes = SceneService().generate_scene(script)

            print("✅ Scene Completed")

            # ======================================
            # VOICE
            # ======================================

            print("\n🎤 STEP 4 : Voice")

            if job_id:
                JobManager.update(job_id, 55, "Generating Voice")

            voice_path = "outputs/audio/voice.wav"

            VoiceService().generate(
                text=script,
                output=voice_path,
                language="hindi_male"
            )

            voice = {
                "audio": voice_path
            }

            print("✅ Voice Completed")

            # ======================================
            # SUBTITLE
            # ======================================

            print("\n💬 STEP 5 : Subtitle")

            if job_id:
                JobManager.update(job_id, 65, "Generating Subtitle")

            subtitle = SubtitleService().generate(
                voice["audio"]
            )

            print("✅ Subtitle Completed")

            # ======================================
            # ASSETS
            # ======================================

            print("\n🖼 STEP 6 : Assets")

            if job_id:
                JobManager.update(job_id, 80, "Downloading Assets")

            assets = AssetService().download(
                keyword=topic,
                count=5
            )

            print("✅ Assets Completed")

            videos = [
                item["path"]
                for item in assets
            ]

            # ======================================
            # COMPOSER
            # ======================================

            print("\n🎥 STEP 7 : Composer")

            if job_id:
                JobManager.update(job_id, 95, "Rendering Video")

            result = ComposerService().generate(
                audio=voice["audio"],
                subtitle=subtitle["subtitle"],
                videos=videos,
                output="outputs/final/final_video.mp4"
            )

            print("✅ Composer Completed")

            if job_id:
                JobManager.complete(
                    job_id,
                    result["video"]
                )

            print("\n🎉 AI VIDEO GENERATED SUCCESSFULLY")

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

            print("\n❌ WORKFLOW FAILED")
            print(type(e).__name__)
            print(str(e))

            if job_id:
                JobManager.failed(
                    job_id,
                    str(e)
                )

            raise