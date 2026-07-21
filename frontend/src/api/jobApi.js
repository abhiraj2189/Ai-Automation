// frontend/src/api/jobApi.js

import api from "./api";

/*
=========================================
GET SINGLE JOB STATUS
=========================================
*/

export const getJobStatus = async (jobId) => {

    const response = await api.get(`/jobs/${jobId}`);

    return response.data;

};

/*
=========================================
GET ALL JOBS
=========================================
*/

export const getJobs = async () => {

    const response = await api.get("/jobs");

    return response.data;

};

/*
=========================================
DELETE JOB
=========================================
*/

export const deleteJob = async (jobId) => {

    const response = await api.delete(`/jobs/${jobId}`);

    return response.data;

};

/*
=========================================
DOWNLOAD VIDEO
=========================================
*/

export const downloadVideo = async (jobId) => {

    const response = await api.get(

        `/jobs/${jobId}/download`,

        {

            responseType: "blob"

        }

    );

    return response.data;

};

/*
=========================================
CANCEL RUNNING JOB
=========================================
*/

export const cancelJob = async (jobId) => {

    const response = await api.post(

        `/jobs/${jobId}/cancel`

    );

    return response.data;

};