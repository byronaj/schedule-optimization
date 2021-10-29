<template>
  <Modal v-on:close="toggleShowModal">
    <div class="container">
    <header class="modal-card-head">
      <p class="modal-card-title">
        Add Employee
      </p>
      <button class="delete" aria-label="close" @click="toggleShowModal"></button>
    </header>

    <section class="modal-card-body">
      <div class="field">
        <label class="label">
          First Name
        </label>
        <div class="control">
          <input class="input" type="text" ref="fName">
        </div>
      </div>

      <div class="field">
        <label class="label">
          Last Name
        </label>
        <div class="control">
          <input class="input" type="text" ref="lName">
        </div>
      </div>
    </section>

    <footer class="modal-card-foot">
      <button class="button is-success" @click="saveNewEmployee">
        Save changes
      </button>
      <button class="button" aria-label="close" @click="toggleShowModal">
        Cancel
      </button>
    </footer>
      </div>
  </Modal>
</template>

<script>
import Modal from "@/components/Modal";

export default {
  name: "AddEmployee",
  components: { Modal },
  data() {
    return {
      showModal: false,
    }
  },
  methods: {
    toggleShowModal() {
      this.$parent.toggleAddEmployee()
    },
    saveNewEmployee() {
      let fName = this.$refs.fName.value
      let lName = this.$refs.lName.value
      //saveNewEmployee
    },
  }
}
</script>

<style scoped>

</style>