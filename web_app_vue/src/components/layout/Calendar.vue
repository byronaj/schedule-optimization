<script>
import '@fullcalendar/core/vdom' // solves problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import resourceTimelinePlugin from '@fullcalendar/resource-timeline'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

export default {
  components: {
    FullCalendar // make the <FullCalendar> tag available
  },
  data() {
    return {
      calendarOptions: {
        plugins: [ resourceTimelinePlugin, dayGridPlugin, interactionPlugin ],
        initialView: 'resourceTimelineDay',
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        dateClick: this.handleDateClick,
        titleFormat: { // will produce something like "Tuesday, September 18, 2018"
          month: 'long',
          year: 'numeric',
          day: 'numeric',
          weekday: 'long'
        },
        resources:
        [
          {
            id: 'a',
            title: 'Employee Name'
          }
        ],
        events: [
          {
            id: '1',
            resourceId: 'a',
            title: 'Day Shift',
            start: this.currentDate() + 'T10:30:00',
            end: this.currentDate() + 'T20:30:00',
          }
        ]
      }
    }
  },
  methods: {
    currentDate() {
      const current = new Date();
      var d = current.getFullYear() + '-' + (current.getMonth()+1) + '-' + current.getDate();
      return d;
    },
    handleDateClick: function(arg) {
      console.log('date click! ' + arg.dateStr  )
    }
  }
}
</script>
<template>
  <FullCalendar :options="calendarOptions" />
</template>