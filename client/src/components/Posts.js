import {Link} from 'react-router-dom'
import { useState } from 'react'

function Posts({profile, logout, posts, addNewPost}) {

    const postForm = {
        content: '',
        profile_id: profile.id,
        title: ''
    }

    const [form, setForm] =useState(postForm)

    const handleSubmit = (e) => {
        e.preventDefault()
        addNewPost(form)
        setForm(postForm)
    }

    const handleChange = (e) => {
        setForm({...form,[e.target.name]: e.target.value})
    }


    return (
        <div>
             <h2>Welcome {profile.username}</h2>
                <button onClick = {logout}>Logout
                <Link to = '/'></Link>
                </button>
                {posts.map((post) => (
                    <Link to = {`/${profile.username}/posts/${post.id}`}>
                        <h3 key={post.id}>
                            {post.title}
                        </h3>
                    </Link>
                ))}
            <form onSubmit={handleSubmit}>
                <input name = 'title'  placeholder='Title' onChange={handleChange} value={form.title} ></input>
                <textarea name='content' rows='10' col='20' warp='hard' maxLength='2000' placeholder='Write Post Here' onChange={handleChange} value={form.content} ></textarea>
                <button type='submit'>Submit</button>
            </form>
        </div>
    )
}

export default Posts

