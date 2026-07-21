export default function Button({

    children,

    onClick,

    type="button",

    variant="primary",

    disabled=false

}){

    const styles={

        primary:"bg-cyan-500 hover:bg-cyan-600",

        secondary:"bg-zinc-800 hover:bg-zinc-700",

        danger:"bg-red-600 hover:bg-red-700"

    };

    return(

        <button

            type={type}

            disabled={disabled}

            onClick={onClick}

            className={`

            px-6

            py-3

            rounded-xl

            font-semibold

            transition

            ${styles[variant]}

            disabled:opacity-50

            `}

        >

            {children}

        </button>

    );

}