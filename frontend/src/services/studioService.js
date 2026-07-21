import api from "./apiClient";

export async function generateVideo(data){

    const res=await api.post(

        "/studio/generate",

        data

    );

    return res.data;

}

export async function getStatus(jobId){

    const res=await api.get(

        `/studio/status/${jobId}`

    );

    return res.data;

}

export async function downloadVideo(jobId){

    return `http://127.0.0.1:8000/studio/download/${jobId}`;

}