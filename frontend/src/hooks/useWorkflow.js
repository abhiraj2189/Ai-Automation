import {
    useEffect,
    useState
} from "react";


export default function useWorkflow(jobId){


const [progress,setProgress]=useState(null);



useEffect(()=>{


if(!jobId)
return;



const ws=new WebSocket(

`ws://127.0.0.1:8000/ws/${jobId}`

);



ws.onmessage=(event)=>{


const data=JSON.parse(
event.data
);


setProgress(data);


};



return ()=>{

ws.close();

};



},[jobId]);



return progress;


}