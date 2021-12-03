<template>
	<div id="constraints">
		<div id="c_top">Global Constraints</div>
		<table class="table" style="margin: 0px auto">
			<tr>
				<th>Day</th>
				<th>1st</th>
				<th>2nd</th>
				<th>3rd</th>
			</tr>
			<tr v-for="(constraint, index) in this.$store.state.globalconstraints" :key="index" @shiftsSaved="getShiftCov">
				<td>{{constraint[3]}}</td>
				<td>{{constraint[0]}}</td>
				<td>{{constraint[1]}}</td>
				<td>{{constraint[2]}}</td>
			</tr>
		</table>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'DisplayConstraints',
	data() {
		return {
			constraints: [
				[0, 0, 0, "Monday"],
				[0, 0, 0, "Tuesday"],
				[0, 0, 0, "Wednesday"],
				[0, 0, 0, "Thursday"],
				[0, 0, 0, "Friday"],
				[0, 0, 0, "Saturday"],
				[0, 0, 0, "Sunday"],
			],
		};
	},
	computed: {
		monShift() { return this.$store.state.globalconstraints[0]; },
		tueShift() { return this.$store.state.globalconstraints[1]; },
		wedShift() { return this.$store.state.globalconstraints[2]; },
		thuShift() { return this.$store.state.globalconstraints[3]; },
		friShift() { return this.$store.state.globalconstraints[4]; },
		satShift() { return this.$store.state.globalconstraints[5]; },
		sunShift() { return this.$store.state.globalconstraints[5]; },
	},
	watch: {
		monShift(newVal, oldVal) { this.constraints[0].value = this.$store.state.globalconstraints[0]; },
		tueShift(newVal, oldVal) { this.constraints[1].value = this.$store.state.globalconstraints[1]; },
		wedShift(newVal, oldVal) { this.constraints[2].value = this.$store.state.globalconstraints[2]; },
		thuShift(newVal, oldVal) { this.constraints[3].value = this.$store.state.globalconstraints[3]; },
		friShift(newVal, oldVal) { this.constraints[4].value = this.$store.state.globalconstraints[4]; },
		satShift(newVal, oldVal) { this.constraints[5].value = this.$store.state.globalconstraints[5]; },
		sunShift(newVal, oldVal) { this.constraints[5].value = this.$store.state.globalconstraints[5]; },
	},
	mounted() {
		this.getShiftCov();
		//update constraints from storage
		this.constraints[0].value = this.$store.state.globalconstraints[0];
		this.constraints[1].value = this.$store.state.globalconstraints[1];
		this.constraints[2].value = this.$store.state.globalconstraints[2];
		this.constraints[3].value = this.$store.state.globalconstraints[3];
		this.constraints[4].value = this.$store.state.globalconstraints[4];
		this.constraints[5].value = this.$store.state.globalconstraints[5];
		this.constraints[6].value = this.$store.state.globalconstraints[6];
	},
	methods: {
		getShiftCov() {
		axios
			.get(`/api/v1/coverages/1/`)
			.then((response) => {
				try {
				this.weekly_cover_instance = response.data
				this.$store.state.globalconstraints[0] = [response.data.mon_shift1, response.data.mon_shift2, response.data.mon_shift3, "Monday"]
				console.log(response.data)
				this.$store.state.globalconstraints[1] = [response.data.tue_shift1, response.data.tue_shift2, response.data.tue_shift3, "Tuesday"]
				this.$store.state.globalconstraints[2] = [response.data.wed_shift1, response.data.wed_shift2, response.data.wed_shift3, "Wednesday"]
				this.$store.state.globalconstraints[3] = [response.data.thu_shift1, response.data.thu_shift2, response.data.thu_shift3, "Thursday"]
				this.$store.state.globalconstraints[4] = [response.data.fri_shift1, response.data.fri_shift2, response.data.fri_shift3, "Friday"]
				this.$store.state.globalconstraints[5] = [response.data.sat_shift1, response.data.sat_shift2, response.data.sat_shift3, "Saturday"]
				this.$store.state.globalconstraints[6] = [response.data.sun_shift1, response.data.sun_shift2, response.data.sun_shift3, "Sunday"]
				console.log(this.$store.state.globalconstraints)
				}
				catch (ex) { console.log(ex) }

			})
			.catch((error) => {
				console.log(JSON.stringify(error));
			});
		},
	}
};
</script>

<style>
	#constraints {
		margin-top: 15px;
	}
	#constraints #c_top {
		border-bottom: 1px solid #000;
		margin: 0 auto;
		text-align: center;
	}
	#constraints #c_list {
		padding-left: 10px;
	}
	#constraints table td {
		font-size: 14px;
	}
	#constraints table tr td:not(:first-child) {
		text-align: center;
	}
	#constraints table th {
		font-size: 15px;
	}
</style>
