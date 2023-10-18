import {useState} from 'react'
import RegisterHome from './RegisterHome'

function Home({attemptLogin, attemptSignup}) {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleUsername = e => setUsername(e.target.value)
    const handlePassword = e => setPassword(e.target.value)

    function handleLogin(e) {
        e.preventDefault()
        attemptLogin({username, password})
        
    }

    return (
        <div>
            <form onSubmit = {handleLogin}>

                <h1>Login</h1>
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

                <input type = 'submit' value = 'Login' /> 

            </form>
            <RegisterHome attemptSignup = {attemptSignup}/>
        </div>
    )
}

export default Home