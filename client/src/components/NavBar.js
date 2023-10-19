import {NavLink} from "react-router-dom";

function NavBar ()  {
    return (
        <nav className="navbar">
            <NavLink className="links" to="/posts">Main Feed</NavLink>
            <NavLink className="links" to="/:username/posts">My Posts</NavLink>
        </nav>
    )
}

export default NavBar;