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
        <div className='text-center '>
             <h2 className='text-5xl font-bold underline'>Welcome {profile.username}</h2>
                {posts.map((post) => (
                    <Link to = {`/${profile.username}/posts/${post.id}`} className='m-20 underline font-bold'>
                        <h3 key={post.id}>
                            {post.title}
                        </h3>
                    </Link>
                ))}
            <form onSubmit={handleSubmit} className='flex flex-col spece-y-2'>
                <input name = 'title'  placeholder='Title' onChange={handleChange} value={form.title} ></input>
                <textarea name='content' rows='10' col='20' warp='hard' maxLength='2000' placeholder='Write Post Here' onChange={handleChange} value={form.content} ></textarea>
                <button type='submit' className='underline text-2xl'>Submit</button>
            </form>
            <button onClick = {logout} className='text-3xl underline mt-10'>Logout
                <Link to = '/'></Link>
            </button>
        </div>
    )
}

export default Posts

