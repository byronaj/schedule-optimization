<script>
import '@fullcalendar/core/vdom' // solves problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import resourceTimelinePlugin from '@fullcalendar/resource-timeline'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
import adaptivePlugin from '@fullcalendar/adaptive'

import axios from 'axios'

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
  mounted() {
    this.getEmployees()
  },
  methods: {
    currentDate() {
      let date_ob = new Date();
      let date = ("0" + date_ob.getDate()).slice(-2);
      let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
      let year = date_ob.getFullYear();
      let current = year + "-" + month + "-" + date;
      //was using 'let current = new Date().toISOString().split('T')[0]'
      //but this was causing some issue with last 4 hours showing as next day
      return current;
    },
    handleDateClick: function(arg) {
      console.log('date click! ' + arg.dateStr  )
    },
    changeDate(date) {
      let cal = this.$refs.FC.getApi()
      cal.gotoDate(date)
    },
    getTestTime(shift, fte) {
      let time = ["", ""]
      if (shift == 0) {
        shift = Math.floor(Math.random() * 3) + 1
      }
      switch (shift) {
        case 1:
          let st = Math.floor(Math.random() * 9) + 1
          let en = Math.round(st + (8*parseFloat(fte)))
          time[0] = st + ":00:00"
          time[1] = en + ":00:00"
          if (st < 10) {time[0] = '0' + time[0];}
          if (en < 10) {time[1] = '0' + time[1];}
          break;
        case 2:
          st = Math.floor(Math.random() * 6) + 9
          en = Math.round(st + (8*parseFloat(fte)))
          time[0] = st + ":00:00"
          time[1] = en + ":00:00"
          if (st < 10) {time[0] = '0' + time[0];}
          break;
        case 3:
          st = Math.floor(Math.random() * 4) + 16
          en = Math.round(st + (8*parseFloat(fte)))
          time[0] = st + ":00:00"
          time[1] = "23:59:00"
          break;
      }
      return time
    },
    getEmployees() {
      axios
          .get(`/api/v1/employees/`)
          .then(response => {
            //refresh resources resources
            let cal = this.$refs.FC.getApi()
            let tr = cal.getResources()
            for (let i = 0; i < tr.length; i++) {
              let res = cal.getResourceById(tr[i].id)
              res.remove()
            }
            for (let i = 0; i < response.data.length; i++) {
              //create resource object
              let evCol = ["#04406f", "#740008", "#705000", "#023e1c"]
              let evTit = ["Variable", "First", "Second", "Third"]
              let res = {
                id: response.data[i].id.toString(),
                name: response.data[i].first_name + " " + response.data[i].first_name,
                eventColor: evCol[response.data[i].shift_block],
              }
              let ttime = this.getTestTime(response.data[i].shift_block, response.data[i].fte)
              let ev = {
                id: response.data[i].id.toString(),
                resourceId: response.data[i].id.toString(),
                title: evTit[response.data[i].shift_block] + ' Shift',
                start: this.currentDate() + 'T' + ttime[0],
                end: this.currentDate() + 'T' + ttime[1],
                borderColor: '#000',
              }
              console.log(ev)
              //add object to calendar
              cal.addResource(res)
              cal.addEvent(ev)
            }
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>
<template>
  <FullCalendar :options="calendarOptions" ref="FC"/>
</template>