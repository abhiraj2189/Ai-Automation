import { Toaster } from "react-hot-toast";

export default function ToastProvider(){

    return(

        <Toaster

            position="top-right"

            reverseOrder={false}

            toastOptions={{

                duration:3000,

                style:{

                    background:"#18181b",

                    color:"#fff",

                    border:"1px solid #27272a"

                }

            }}

        />

    );

}