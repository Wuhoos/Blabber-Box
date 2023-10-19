import {Link} from 'react-router-dom'
import { useState } from 'react'

function Posts({profile, logout, posts, addNewPost}) {

    const defalut = {
        content: ''
    }

    const [form, setForm] =useState(defalut)

    const handleSubmit = (e) => {
        e.preventDefault()
        addNewPost(form)
        setForm(defalut)
    }

    const handleChange = (e) => {
        setForm({...form,[e.target.name]: [e.target.value]})
    }


    return (
        <div>
             <h2>Welcome {profile.username}</h2>
                <button onClick = {logout}>Logout
                <Link to = '/'></Link>
                </button>
                {posts.map(({id, content}) => (
                    <li key={id}>
                        <h3>
                            <Link to = {`/${profile.username}/posts/${id}`} key={id}> 
                                {content} 
                            </Link>
                        </h3>
                    </li>
                ))}
            <form onSubmit={handleSubmit}>
                <textarea name='content' rows='10' col='20' warp='hard' maxLength='2000' placeholder='Write Post Here' onChange={handleChange} value={form.content} ></textarea>
                <button type='submit'>Submit</button>
            </form>
        </div>
    )
}

export default Posts

