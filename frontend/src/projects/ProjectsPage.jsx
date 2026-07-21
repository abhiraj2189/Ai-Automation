import PageHeader from "../components/common/PageHeader";
import ProjectToolbar from "./components/ProjectToolbar";
import ProjectStats from "./components/ProjectStats";
import ProjectGrid from "./components/ProjectGrid";

export default function ProjectsPage(){

    return(

        <div className="space-y-8">

            <PageHeader

                title="Projects"

                subtitle="Manage your AI Projects"

            />

            <ProjectStats/>

            <ProjectToolbar/>

            <ProjectGrid/>

        </div>

    );

}