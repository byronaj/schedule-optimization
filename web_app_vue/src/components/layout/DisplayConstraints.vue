<template>
  <div id="constraints">
      <div id="c_top">
          Global Constraints
      </div>
      <div id="c_list">
          <ul>
              <li v-for="(item) in this.$store.state.globalconstraints">
                  {{item[0]}} - {{item[1]}}
              </li>
          </ul>
      </div>
  </div>
</template>

<script>
export default {
    name: 'DisplayConstraints',
    data() {
        return {
            constraints: [
                {title: "Maximum shift hours", value: 8},
                {title: "Maximum consecutive working days", value: 5},
                {title: "Minimum consecutive working days", value: 2},
                {title: "Minimum consecutive free days", value: 2},
                {title: "Maximum consecutive weekends", value: 2},
                {title: "Allow Back 2 Back shifts", value: true},
            ]
        }
    },
    computed: {
        shifthours() { return this.$store.state.globalconstraints[0][1] },
        maxwork() { return this.$store.state.globalconstraints[1][1] },
        minwork() { return this.$store.state.globalconstraints[2][1] },
        minfree() { return this.$store.state.globalconstraints[3][1] },
        maxweekend() { return this.$store.state.globalconstraints[4][1] },
        back2back() { return this.$store.state.globalconstraints[5][1] },
    },
    watch: {
        shifthours (newVal, oldVal) { this.constraints[0].value = this.$store.state.globalconstraints[0][1]; },
        maxwork (newVal, oldVal) { this.constraints[1].value = this.$store.state.globalconstraints[1][1]; },
        minwork (newVal, oldVal) { this.constraints[2].value = this.$store.state.globalconstraints[2][1]; },
        minfree (newVal, oldVal) { this.constraints[3].value = this.$store.state.globalconstraints[3][1]; },
        maxweekend (newVal, oldVal) { this.constraints[4].value = this.$store.state.globalconstraints[4][1]; },
        back2back (newVal, oldVal) { this.constraints[5].value = this.$store.state.globalconstraints[5][1]; },
    },
    mounted() {
      //update constraints from storage
      this.constraints[0].value = this.$store.state.globalconstraints[0][1];
      this.constraints[1].value = this.$store.state.globalconstraints[1][1];
      this.constraints[2].value = this.$store.state.globalconstraints[2][1];
      this.constraints[3].value = this.$store.state.globalconstraints[3][1];
      this.constraints[4].value = this.$store.state.globalconstraints[4][1];
      this.constraints[5].value = this.$store.state.globalconstraints[5][1];
  }
}
</script>

<style>
#constraints {
    margin-top: 50px;
}
#constraints #c_top {
    border-bottom: 1px solid #000;
    margin:0 auto;
    text-align: center;
}
#constraints #c_list {
    padding-left: 10px;
}
</style>