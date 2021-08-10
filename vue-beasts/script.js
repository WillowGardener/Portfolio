new Vue({
    el: '#root',
    data: {
        
        enemyStats: {
            health: 100,
            attack: 15,
            defense: 12,
            attacks: ['lavaBall','pollute','curlUp','timeBomb']
        },
        myStats: {
            health: 100,
            attack: 12,
            defense: 15,},
        myLastAttackMessage: '',
        enemyLastAttackMessage: '',
    },
    methods: {
        sparkleStrike: function() {
            let damage = 20 + this.myStats.attack - this.enemyStats.defense
            this.enemyStats.health -= damage
            if (this.enemyStats.health < 0) {
                this.enemyStats.health = 0
            }
            this.myLastAttackMessage = `You used sparkle strike! You dealt ${damage} damage!`
            this.enemyAttack()
        },
        heckinChomp: function() {
            let damage = 10 + this.myStats.attack - this.enemyStats.defense
            this.enemyStats.health -= damage
            this.enemyStats.attack -= 5
            if (this.enemyStats.health < 0) {
                this.enemyStats.health = 0
            }
            this.myLastAttackMessage = `You heckin chomped em! You dealt ${damage} damage and lowered the enemy's attack!`
        },
        flippyFlap: function() {

        },
        strut: function() {
            this.myStats.attack += 5
            this.myLastAttackMessage = `You strutted your stuff! You are so confident, your attack went up!`
        },
        lavaBall: function() {
            let damage = 10 + this.enemyStats.attack - this.myStats.defense
            this.myStats.health -= damage
            this.enemyLastAttackMessage = `the enemy used lava ball! It dealt ${damage} damage!`
        },
        pollute: function() {

        },
        curlUp: function() {

        },
        timeBomb: function() {

        },
        enemyMove: function() {
            attacks = [this.lavaBall(),this.pollute(),this.curlUp(),this.timeBomb()]
            let attackChoice = attacks[Math.floor(Math.random()*4)]
            attackChoice
            
        },
        runTurn: function(text) {
            console.log(text)
        } 
    }
})