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
        <>
            <h1>{displayedPost.title}</h1>
            <p>{displayedPost.content}</p>
        </>
    )
}





export default PostCard