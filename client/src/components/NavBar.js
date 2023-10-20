import {NavLink} from "react-router-dom";

function NavBar ({ profile })  {
    console.log(profile)
    return (
        <nav className="navbar">
            <NavLink className="links" to="/posts">Main Feed</NavLink>
            <NavLink className="links" to={`/${profile.username}/posts`}>My Posts</NavLink>
        </nav>
    )
}

export default NavBar;