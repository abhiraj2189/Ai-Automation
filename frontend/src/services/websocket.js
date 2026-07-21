export class WorkflowSocket{

    constructor(){

        this.ws=null;

    }

    connect(jobId,onMessage){

        this.ws=new WebSocket(

            `ws://127.0.0.1:8000/ws/${jobId}`

        );

        this.ws.onmessage=(event)=>{

            const data=JSON.parse(event.data);

            onMessage(data);

        };

    }

    disconnect(){

        if(this.ws){

            this.ws.close();

        }

    }

}