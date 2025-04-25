<script>
  import { Router, Route } from 'svelte-routing';
  import Home from './pages/Home.svelte';
  import Booking from './pages/Booking.svelte';
  import Contact from './pages/Contact.svelte';
  import Shop from './pages/Shop.svelte';
  import EmployeePortal from './pages/EmployeePortal.svelte';
  import Login from './components/Login.svelte';
  import './App.css';
</script>

<main class="bg-spaNavy text-white min-h-screen">
  <nav class="bg-spaGold p-4">
    <ul class="flex gap-6 justify-center">
      <li><a href="/" class="hover:underline">Home</a></li>
      <li><a href="/booking" class="hover:underline">Book Now</a></li>
      <li><a href="/contact" class="hover:underline">Contact</a></li>
      <li><a href="/shop" class="hover:underline">Shop</a></li>
      <li><a href="/employee" class="hover:underline">Employee Portal</a></li>
      <li><a href="/login" class="hover:underline">Login</a></li>
    </ul>
  </nav>
  <Router>
    <div class="container mx-auto p-4">
      <Route path="/" component={Home} />
      <Route path="/booking" component={Booking} />
      <Route path="/contact" component={Contact} />
      <Route path="/shop" component={Shop} />
      <Route path="/employee" component={EmployeePortal} />
      <Route path="/login" component={Login} />
    </div>
  </Router>
  <footer class="bg-spaNavy animated-bg py-8">
    <div class="max-w-6xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
      <!-- Logo -->
      <div class="mb-4 md:mb-0">
        <img src="/logo.png" alt="Spa Serenity Logo" class="h-16" />
      </div>
      <!-- Social Media Links -->
      <div class="flex gap-4">
        <a href="https://x.com/spa_serenity" target="_blank" rel="noopener noreferrer">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
            <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
          </svg>
        </a>
        <a href="https://reddit.com/r/spa_serenity" target="_blank" rel="noopener noreferrer">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 0C5.373 0 0 5.373 0 12c0 3.314 1.343 6.314 3.515 8.485l-2.036 2.036C.567 23.433 0 24.7 0 26h7.433c.445-1.778 2.133-3.111 4.089-3.111s3.644 1.333 4.089 3.111H24c0-1.3-.567-2.567-1.478-3.478l-2.036-2.036C22.657 18.314 24 15.314 24 12c0-6.627-5.373-12-12-12zm0 18.667c-1.473 0-2.667-1.194-2.667-2.667S10.527 13.333 12 13.333s2.667 1.194 2.667 2.667S13.473 18.667 12 18.667zm4.667-6.667c0 1.473-1.194 2.667-2.667 2.667S11.333 13.473 11.333 12 12.527 9.333 14 9.333s2.667 1.194 2.667 2.667z"/>
          </svg>
        </a>
        <a href="https://linkedin.com/company/spa-serenity" target="_blank" rel="noopener noreferrer">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
            <path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/>
          </svg>
        </a>
        <a href="weixin://dl/business/?t=spa_serenity" target="_blank" rel="noopener noreferrer">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
            <path d="M9.663 8.76c-.664 0-1.232.568-1.232 1.232 0 .664.568 1.232 1.232 1.232.664 0 1.232-.568 1.232-1.232 0-.664-.568-1.232-1.232-1.232zm4.672 0c-.664 0-1.232.568-1.232 1.232 0 .664.568 1.232 1.232 1.232.664 0 1.232-.568 1.232-1.232 0-.664-.568-1.232-1.232-1.232zm-2.335 8.205c-3.99 0-7.328-2.702-8.205-6.335-.234 1.232-.117 2.464.234 3.696.585 2.114 2.232 3.862 4.346 4.447-.585-1.232-1.232-3.112-.936-4.808zm12-5.465c0 6.627-5.373 12-12 12s-12-5.373-12-12 5.373-12 12-12 12 5.373 12 12zm-8.205 6.335c-.877 3.633-4.215 6.335-8.205 6.335.296 1.696.936 3.576.936 4.808 2.114-.585 3.761-2.333 4.346-4.447.351-1.232.468-2.464.234-3.696zm2.205-10.935c-.664 0-1.232.568-1.232 1.232 0 .664.568 1.232 1.232 1.232.664 0 1.232-.568 1.232-1.232 0-.664-.568-1.232-1.232-1.232zm-4.672 0c-.664 0-1.232.568-1.232 1.232 0 .664.568 1.232 1.232 1.232.664 0 1.232-.568 1.232-1.232 0-.664-.568-1.232-1.232-1.232z"/>
          </svg>
        </a>
        <a href="https://discord.gg/spa_serenity" target="_blank" rel="noopener noreferrer">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
            <path d="M20.317 4.3698a19.7913 19.7913 0 00-4.8851-1.5152.0741.0741 0 00-.0785.0371c-.211.433-.4261.9147-.6508 1.4037a18.3378 18.3378 0 00-5.7448 0c-.225-.489-.4399-.9707-.6508-1.4037a.075.075 0 00-.0785-.0371 19.7363 19.7363 0 00-4.8851 1.5152.0699.0699 0 00-.0321.0277C.5336 9.0458-.319 13.5799.0992 18.0578a.0824.0824 0 00.0312.0561 19.9744 19.9744 0 005.9933 3.0307.077.077 0 00.0842-.0286c.4616-.6894.9199-1.4274 1.3648-2.2264a.076.076 0 00-.0415-.1056 13.5219 13.5219 0 01-1.9308-.6941.0741.0741 0 01-.0404-.0699.0707.0707 0 01.0193-.0528c.1303-.1119.262-.2218.3937-.3307a.0747.0747 0 01.0791-.0107 13.7579 13.7579 0 0010.2813 0 .0759.0759 0 01.0791.0107c.1317.1089.2634.2188.3937.3307a.071.071 0 01.0193.0528.0754.0754 0 01-.0404.0699 13.6783 13.6783 0 01-1.9308.6941.0757.0757 0 00-.0415.1056c.4449.799 .9032 1.537 1.3648 2.2264a.0766.0766 0 00.0842.0286 19.9277 19.9277 0 005.9933-3.0307.0783.0783 0 00.0312-.0561c.5007-5.177-.8382-9.6738-3.5485-13.6604a.061.061 0 00-.0321-.0277zM8.02 15.3312c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9555-2.4189 2.1569-2.4189 1.2102 0 2.1757 1.0952 2.1569 2.4189 0 1.3332-.9464 2.419-2.1569 2.419zm7.9748 0c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9555-2.4189 2.1569-2.4189 1.2102 0 2.1757 1.0952 2.1569 2.4189 0 1.3332-.9464 2.419-2.1569 2.419z"/>
          </svg>
        </a>
      </div>
    </div>
    <p class="text-center mt-4 text-sm">© 2025 Spa Serenity. All rights reserved.</p>
  </footer>
</main>

<style>
  .animated-bg {
    background: linear-gradient(45deg, #1A2A44, #D4AF37, #1A2A44);
    background-size: 200% 200%;
    animation: gradient 15s ease infinite;
  }

  @keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
</style>
