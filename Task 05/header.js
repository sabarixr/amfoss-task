class HeaderComponent extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <div class="top-bar">
        <div class="logo">
          <img src="topbar/logo.svg" >
        </div>
        <ul class="socials">
          <li><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q?si=w5A77LELTgmTbXcTcd2Qag"><img src="topbar/spotify.svg"></a></li>
          <li><a href="https://www.youtube.com/@ImagineDragons"><img src="topbar/youtube.svg"></a></li>
          <li><a href="https://twitter.com/imaginedragons"><img src="topbar/twitter.svg"></a></li>
          <li><a href="https://www.instagram.com/imaginedragons/"><img src="topbar/instagram.svg"></a></li>
        </ul>
      </div>
    `;
  }
}


customElements.define('header-icons', HeaderComponent);

