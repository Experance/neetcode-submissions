class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert string to have no spaces, and only letters and numbers (isalnum())
        # use two pointer, going from each end inward, checking if each letter isalnum() and if not comparing, else
        #   adjust pointer accordingly
        s = s.lower() # make all lowercase
        
        start_index = 0
        end_index = len(s) - 1
        failed = False

        while start_index <= end_index:
            failed = False
            if not s[start_index].isalnum():
                start_index += 1
                failed = True
            if not s[end_index].isalnum():
                end_index -= 1
                failed = True

            if (failed):
                continue

                
            #print(s[end_index])
            if s[start_index].lower() != s[end_index].lower(): # compare the now correct strings
                return False
            

            # move loop forward
            start_index += 1
            end_index -= 1
            
            
            
        return True


        # while start_index <= end_index:
            
        #     # get to a non alnum value for start
        #     while start_index <= end_index and not s[start_index].isalnum():
        #         start_index += 1
                
        #     #print(s[start_index])
        #     # get to a non alnum value for end
        #     while start_index <= end_index and not s[end_index].isalnum():
        #         end_index -= 1
                
        #     #print(s[end_index])
        #     if start_index <= end_index and s[start_index] != s[end_index]: # compare the now correct strings
        #         return False
            

        #     # move loop forward
        #     start_index += 1
        #     end_index -= 1
            
            
            
        # return True
            