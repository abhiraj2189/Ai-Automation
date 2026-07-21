import { createContext, useEffect, useState } from "react";

export const ThemeContext=createContext();

export default function ThemeProvider({children}){

const [dark,setDark]=useState(true);

useEffect(()=>{

if(dark){

document.documentElement.classList.add("dark");

}else{

document.documentElement.classList.remove("dark");

}

},[dark]);

return(

<ThemeContext.Provider

value={{

dark,

toggleTheme:()=>setDark(!dark)

}}

>

{children}

</ThemeContext.Provider>

);

}