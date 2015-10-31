def factorize(given)
    cache = Hash.new(-1)
    # Sorts array and gets factors for each index in arr.
    given.sort!.each_index { |i| get_factors(given, i, cache) }
    print given
    print "\n"
    given.each_index {|i| print (given[i].to_s + " => " + cache[given[i]].to_s + "\n")}

end

def get_factors(given, ind,cache)
    if cache.key?(given[ind]) == false
        cache[given[ind]] = []  # set up array of factors in cache
        #sorted array means that only elements before a certain element can be factors so down to 0 from current index
        ind.downto(0) { |i| put_in(cache, given[i], given[ind]) }
    end
end

def put_in(cache, n, target)
    # Skip calculation if it's already in the cache.
    if cache[target].index(n) != nil
        return
    end
    # Add elem of array to cache at target if it is a factor.
    if target % n == 0 && target != n
        cache[target].push(n)
        # push all it's other factors to the array as well
        if cache[n].length != 0
            cache[target].push(cache[n])
            cache[target].flatten!.uniq!
        end
    end
end

factorize([2, 3, 5, 10, 15, 100, 500, 1500])
factorize([10, 5, 10, 2, 20])