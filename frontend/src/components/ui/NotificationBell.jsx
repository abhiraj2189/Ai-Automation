import { FaBell } from "react-icons/fa";

export default function NotificationBell(){

return(

<button

className="

relative

"

>

<FaBell

className="text-xl"

/>

<span

className="

absolute

-top-1

-right-1

bg-red-500

w-2

h-2

rounded-full

"

/>

</button>

);

}