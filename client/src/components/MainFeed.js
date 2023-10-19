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
        <div>

             <h2>Main Feed</h2>
                <button onClick = {logout}>Logout
                <Link to = '/'></Link>
                </button>
                {allPosts.map((post) => (
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

export default MainFeed