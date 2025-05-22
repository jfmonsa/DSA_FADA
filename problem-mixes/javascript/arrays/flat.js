export function flat(arr, depth = Infinity){
    if (depth === 0) return arr.slice()
    return arr.reduce((acc, elm) => {
        if (Array.isArray(elm) && depth > 0){
            return [...acc, ...flat(elm, depth -1 )]
        } else {
            return [...acc, elm]
        }
    }, [])
}
