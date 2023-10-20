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
        <div className='setScreen text-center bg-gray-300'>
            <h1 className='text-6xl font-bold bg-green-500 text-pink-400'>Blabber Box</h1>
            <form onSubmit = {handleLogin} className='m-20 flex flex-col space-y-4'>
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

                <input type = 'submit' value = 'Login' className="text-3xl font-bold underline" /> 

            </form>
            <RegisterHome attemptSignup = {attemptSignup}/>
        </div>
    )
}

export default Home