import {Link} from 'react-router-dom'
import { useState, useEffect } from 'react'

function MainFeed({profile, logout, addNewPost}){

    const [allPosts, setAllPosts] = useState([])

    useEffect(() => {
        fetch ('/posts')
        .then(res => res.json())
        .then(data => setAllPosts(data))
    }, [])

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
        <div className='text-center grid gap-y-6 setScreen bg-gray-300'>

             <h2 className='font-bold text-6xl bg-gray-400'>Main Feed</h2>
                <div className='grid grid-cols-3 gap-4 gap-y-6 underline text-2xl' >
                    {allPosts.map((post) => (
                        <Link to = {`/${profile.username}/posts/${post.id}`}>
                            <h3 key={post.id}>
                                {post.title}
                            </h3>
                        </Link>
                    ))}
                </div>
                
            <form onSubmit={handleSubmit} className='flex flex-col justify-center'>
                <input name = 'title'  placeholder='Title' onChange={handleChange} value={form.title} className='mb-2 rounded-md'></input>
                <textarea name='content' 
                rows='10' 
                col='20' 
                warp='hard' 
                maxLength='2000' 
                placeholder='Write Post Here' 
                onChange={handleChange} 
                value={form.content}
                className='rounded-md'
                 ></textarea>
                <button type='submit' className='underline font-bold'>Submit</button>
            </form>
            <button onClick = {logout} className='underline font-bold'>Logout
                <Link to = '/'></Link>
            </button >
        </div>
    )
}

export default MainFeed