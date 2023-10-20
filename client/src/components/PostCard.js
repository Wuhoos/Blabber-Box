import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'


function PostCard({ profile }) {
    const [displayedPost, setDisplayedPost] = useState({})
    const params = useParams()

    useEffect(() => {
        fetch(`/${profile.username}/posts/${params.id}`)
            .then(response => {
                if (response.ok) {
                    response.json()
                        .then(data => setDisplayedPost(data))
                }
                else {
                    setDisplayedPost({})
                }
            })
    }, [profile])

    return (
        <div className='setScreen  bg-gray-300 text-center'>
            <h1 className='text-6xl font-bold bg-gray-400'>{displayedPost.title}</h1>
            <p className='mt-8'>{displayedPost.content}</p>
        </div>
    )
}





export default PostCard