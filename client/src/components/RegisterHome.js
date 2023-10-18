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
            <form onSubmit = {handleSignup}>

                <h1>Register</h1>
                <input 
                    type = 'text'
                    onChange = {handleUsername}
                    value = {username}
                    placeholder = 'username'
                />

                <input 
                    type = 'text'
                    onChange = {handlePassword}
                    value = {password}
                    placeholder = 'password'
                />

                <input type = 'submit' value = 'Signup'/>

            </form>
        </div>
    )
}

export default RegisterHome