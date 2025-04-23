<script>
  import { onMount } from 'svelte';
  import FullCalendar from '@fullcalendar/core';
  import dayGridPlugin from '@fullcalendar/daygrid';
  import timeGridPlugin from '@fullcalendar/timegrid';
  import axios from 'axios';

  let calendar;
  let events = [];

  onMount(async () => {
    const calendarEl = document.getElementById('calendar');
    calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: [dayGridPlugin, timeGridPlugin],
      initialView: 'timeGridWeek',
      events: async (info, successCallback) => {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/bookings/`, {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
        });
        successCallback(response.data.map(booking => ({
          title: booking.service.name,
          start: booking.start_time,
          end: booking.end_time,
        })));
      },
      selectable: true,
      select: async info => {
        try {
          await axios.post(`${import.meta.env.VITE_API_URL}/api/bookings/`, {
            service: 1, // Replace with dynamic service ID
            employee: 1, // Replace with dynamic employee ID
            start_time: info.startStr,
            end_time: info.endStr,
          }, {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
          });
          calendar.refetchEvents();
        } catch (error) {
          alert('Booking failed');
        }
      },
    });
    calendar.render();
  });
</script>

<div class="max-w-4xl mx-auto p-4">
  <h2 class="text-2xl mb-4">Book Your Appointment</h2>
  <div id="calendar"></div>
</div>
