import { useEffect, useState } from "react";
import { getJobs } from "../api/jobApi";

export default function Jobs() {

    const [jobs, setJobs] = useState([]);

    const loadJobs = async () => {

        try {

            const data = await getJobs();

            setJobs(data);

        }

        catch(err){

            console.log(err);

        }

    };

    useEffect(()=>{

        loadJobs();

        const timer = setInterval(loadJobs,3000);

        return ()=>clearInterval(timer);

    },[]);

    return (

        <div className="space-y-6">

            <h1 className="text-4xl font-bold">

                AI Jobs

            </h1>

            <table className="w-full">

                <thead>

                    <tr>

                        <th>Job</th>

                        <th>Status</th>

                        <th>Progress</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        jobs.map(job=>(

                            <tr key={job.id}>

                                <td>{job.topic}</td>

                                <td>{job.status}</td>

                                <td>{job.progress}%</td>

                            </tr>

                        ))

                    }

                </tbody>

            </table>

        </div>

    );

}