class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        
        Inbuilt conversion.
        """
        return bin(int(a,2)+int(b,2))[2:]

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        
        Approach:
        
        Fill both strings with zeros depending on the string with maximum length.
        Perform addition from the LSB.
        Modify carry based on the sum at every single addition.
        Example: 1+1 => S=0,C=1
                 1+0 => S=1,C=0
        Do not forget to add the carry at the end if its equal to 1.
        """
        n = max(len(a),len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        ans = []
        
        for i in range(n-1,-1,-1):
            if(a[i]=='1'):
                carry+=1
            if(b[i]=='1'):
                carry+=1
            
            if(carry%2==1):
                ans.append('1')
            else:
                ans.append('0')
            
            carry/=2
        
        if(carry==1):
            ans.append('1')
        
        return ''.join(ans[::-1])
