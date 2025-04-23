<script>
  import { Router, Route } from 'svelte-routing';
  import Home from './pages/Home.svelte';
  import Booking from './pages/Booking.svelte';
  import Contact from './pages/Contact.svelte';
  import Shop from './pages/Shop.svelte';
  import EmployeePortal from './pages/EmployeePortal.svelte';
  import Login from './components/Login.svelte';
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
    <Route path="/" component={Home} />
    <Route path="/booking" component={Booking} />
    <Route path="/contact" component={Contact} />
    <Route path="/shop" component={Shop} />
    <Route path="/employee" component={EmployeePortal} />
    <Route path="/login" component={Login} />
  </Router>
</main>
