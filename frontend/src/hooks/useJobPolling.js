import { useEffect } from "react";
import { getJobStatus } from "../api/jobApi";

export default function useJobPolling(

    jobId,

    onUpdate,

    onComplete

) {

    useEffect(() => {

        if (!jobId) return;

        const timer = setInterval(async () => {

            try {

                const job = await getJobStatus(jobId);

                onUpdate(job);

                if (

                    job.status === "completed" ||

                    job.status === "failed"

                ) {

                    clearInterval(timer);

                    onComplete(job);

                }

            }

            catch (e) {

                console.log(e);

            }

        },2000);

        return ()=>clearInterval(timer);

    },[jobId]);

}