from sys import stdin
    
def ladder():
    buffer = bytearray('a' * 6, encoding='ascii')
    yield buffer.decode()

    for _ in range(5):
        for _ in range(12):
            for _ in range(25):
                buffer[-1] += 1
                yield buffer.decode()

                buffer[-2] += 1
                yield buffer.decode()
        
            buffer[-3] += 1
            yield buffer.decode()
        
            buffer[-4] += 1
            yield buffer.decode()
        
            for _ in range(25):
                buffer[-1] -= 1
                yield buffer.decode()

                buffer[-2] -= 1
                yield buffer.decode()
        
            buffer[-3] += 1
            yield buffer.decode()
        
            buffer[-4] += 1
            yield buffer.decode()

        buffer[-5] += 1
        yield buffer.decode()
        
        buffer[-6] += 1
        yield buffer.decode()

        for _ in range(12):
            for _ in range(25):
                buffer[-1] += 1
                yield buffer.decode()

                buffer[-2] += 1
                yield buffer.decode()
        
            buffer[-3] -= 1
            yield buffer.decode()
        
            buffer[-4] -= 1
            yield buffer.decode()
        
            for _ in range(25):
                buffer[-1] -= 1
                yield buffer.decode()

                buffer[-2] -= 1
                yield buffer.decode()
        
            buffer[-3] -= 1
            yield buffer.decode()
        
            buffer[-4] -= 1
            yield buffer.decode()
        
        buffer[-5] += 1
        yield buffer.decode()
        
        buffer[-6] += 1
        yield buffer.decode()


n = int(stdin.read())
l = ladder()
for _ in range(n):
    print(next(l))
