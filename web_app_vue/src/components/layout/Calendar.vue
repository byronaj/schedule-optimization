<script>
import '@fullcalendar/core/vdom' // solves problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import resourceTimelinePlugin from '@fullcalendar/resource-timeline'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
import adaptivePlugin from '@fullcalendar/adaptive'

export default {
  components: {
    FullCalendar // make the <FullCalendar> tag available
  },
  data() {
    return {
      calendarOptions: {
        plugins: [ resourceTimelinePlugin, dayGridPlugin, interactionPlugin, adaptivePlugin ],
        initialView: 'resourceTimelineDay',
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        dateClick: this.handleDateClick,
        height: '88vh',
        titleFormat: { // will produce something like "Tuesday, September 18, 2018"
          month: 'long',
          year: 'numeric',
          day: 'numeric',
          weekday: 'long'
        },
        editable: true,
        headerToolbar: {
          left: 'title',
          right: '',
        },
        resourceAreaColumns:
        [
          {
            field: 'name',
            headerContent: 'Employees',
          }
        ],
        resourceAreaWidth: '20%',
        resources: [
          {
            id: 'a',
            name: 'Employee Name',
            eventColor: '#511b1b',
            
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
        ],
        eventResize: function(info) {
          alert(info.event.title + " end is now " + info.event.end.toISOString());

          if (!confirm("is this okay?")) {
            info.revert();
          }
        }
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
    },
    changeDate(date) {
      let cal = this.$refs.FC.getApi()
      cal.gotoDate(date)
    }
  }
}
</script>
<template>
  <FullCalendar :options="calendarOptions" ref="FC"/>
</template>