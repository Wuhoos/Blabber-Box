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
        <div className='text-center'>
            <h1 className='text-5xl font-bold underline'>Blabber Box</h1>
            <form onSubmit = {handleLogin} className='m-20 flex flex-col space-y-4'>
                <input 
                    type = 'text'
                    onChange = {handleUsername}
                    value = {username}
                    placeholder = 'username'
                    className='bold'
                />

                <input 
                    type = 'text'
                    onChange = {handlePassword}
                    value = {password}
                    placeholder = 'password'
                />

                <input type = 'submit' value = 'Login' className="text-3xl font-bold underline" /> 

            </form>
            <RegisterHome attemptSignup = {attemptSignup}/>
        </div>
    )
}

export default Home