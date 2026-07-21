export default function Badge({

children,

color="cyan"

}){

return(

<span

className={`

px-3

py-1

rounded-full

text-sm

bg-${color}-500/20

text-${color}-400

`}

>

{children}

</span>

);

}