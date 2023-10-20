import {useState} from 'react'

function RegisterHome({attemptSignup}) {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleUsername = e => setUsername(e.target.value)
    const handlePassword = e => setPassword(e.target.value)

    function handleSignup(e) {
        attemptSignup({username, password})
        e.preventDefault()
    }

    return (
        <div>
            <form onSubmit = {handleSignup} className='m-20 flex flex-col space-y-4'>

                <input 
                    type = 'text'
                    onChange = {handleUsername}
                    value = {username}
                    placeholder = 'username'
                    className='border-4 border-pink-300'
                />

                <input 
                    type = 'text'
                    onChange = {handlePassword}
                    value = {password}
                    placeholder = 'password'
                    className='border-4 border-pink-300'
                />

                <input type = 'submit' value = 'Signup' className="text-3xl font-bold underline"/>

            </form>
        </div>
    )
}

export default RegisterHome