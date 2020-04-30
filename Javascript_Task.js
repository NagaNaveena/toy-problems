function countBs(arg) {
    let len = arg.length
    let ct = 0;
    for(let i =0; i < len; i++) {
        if(arg.charAt(i) === 'B') {
            ct += 1;
        }
    }
    return ct;
}

function countChar(arg, letter) {
    let len = arg.length
    let ct = 0;
    for(let i =0; i < len; i++) {
        if(arg.charAt(i) === letter) {
            ct += 1;
        }
    }
    return ct;
}


function deepEqual(obj , newObject) { 
    let ct = 0;
    const keysFirst = Object.keys(obj)
    const keysSecond = Object.keys(newObject)
    if(keysFirst.length === keysSecond.length) {
        for(let i =0; i < keysFirst.length; i++) {
            const keyF = keysFirst[i]
            const keyS = keysSecond[i]
            if((typeof keyF === typeof keyS)  && (typeof obj[keyF] === 'object')) {
                if(deepEqual(obj[keyF],newObject[keyS])) {
                    ct += 1;
                }
            }
            else if(keyF === keyS) {
                if(obj[keyF] === newObject[keyS]) {
                    ct += 1
                }
            }
            else {
                return false
            }    
        }
        if(ct === keysFirst.length) {
            return true
        }
        return false
    }
    else {
        return false
    }
}

obj1 = {
    a:'1',
    c:'2',
    b: {
        x: '1',
        y: '2'
    }
}
obj2 = {
    c:'2',
    a:'1'

}
console.log(deepEqual(obj1,obj2))
